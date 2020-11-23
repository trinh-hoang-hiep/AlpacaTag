import Vue from 'vue';
import VTooltip from 'v-tooltip';
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

import annotationMixin from './mixin';
import HTTP from './http';
import simpleShortcut from './filter';

Vue.use(VTooltip);
Vue.use(Loading);
Vue.use(require('vue-shortkey'), {
  prevent: ['input', 'textarea'],
});

Vue.filter('simpleShortcut', simpleShortcut);

Vue.component('annotator', {
  template: '<div @click="setSelectedRange">\
                    <span class="text-sequence"\
                         v-for="r in chunks"\
                         v-if="id2label[r.label]"\
                         v-bind:class="{tag: id2label[r.label].text_color}"\
                         v-bind:style="{ color: id2label[r.label].text_color, backgroundColor: id2label[r.label].background_color, textDecoration: id2label[r.label].text_decoration}"\
                    >{{ text.slice(r.start_offset, r.end_offset) }}<button class="delete is-small"\
                                         v-if="id2label[r.label].text_color"\
                                         @click="removeLabel(r)"></button></span>\
               </div>',
  props: {
    labels: Array, // [{id: Integer, color: String, text: String}]
    text: String,
    entityPositions: Array, // [{'startOffset': 10, 'endOffset': 15, 'label_id': 1}]
    recommendPositions: Array,
  },
  data() {
    return {
      startOffset: 0,
      endOffset: 0,
    };
  },

  methods: {
    setSelectedRange(e) {
      let start;
      let end;
      if (window.getSelection) {
        const range = window.getSelection().getRangeAt(0);
        const preSelectionRange = range.cloneRange();
        preSelectionRange.selectNodeContents(this.$el);
        preSelectionRange.setEnd(range.startContainer, range.startOffset);
        start = preSelectionRange.toString().length;
        end = start + range.toString().length;
      } else if (document.selection && document.selection.type !== 'Control') {
        const selectedTextRange = document.selection.createRange();
        const preSelectionTextRange = document.body.createTextRange();
        preSelectionTextRange.moveToElementText(this.$el);
        preSelectionTextRange.setEndPoint('EndToStart', selectedTextRange);
        start = preSelectionTextRange.text.length;
        end = start + selectedTextRange.text.length;
      }
      this.startOffset = start;
      this.endOffset = end;
      console.log(start, end);
    },

    duplicateRange(){
      for (let i = 0; i < this.entityPositions.length; i++) {
        const e = this.entityPositions[i];
        if ((e.start_offset == this.startOffset) && (e.end_offset == this.endOffset)) {
          return e;
        }
      }
      return false;
    },

    validRange() {
      if (this.startOffset === this.endOffset) {
        return false;
      }
      if (this.startOffset > this.text.length || this.endOffset > this.text.length) {
        return false;
      }
      if (this.startOffset < 0 || this.endOffset < 0) {
        return false;
      }
      for (let i = 0; i < this.entityPositions.length; i++) {
        const e = this.entityPositions[i];
        if ((e.start_offset <= this.startOffset) && (this.startOffset < e.end_offset)) {
          return false;
        }
        if ((e.start_offset < this.endOffset) && (this.endOffset < e.end_offset)) {
          return false;
        }
        if ((this.startOffset < e.start_offset) && (e.start_offset < this.endOffset)) {
          return false;
        }
        if ((this.startOffset < e.end_offset) && (e.end_offset < this.endOffset)) {
          return false;
        }
      }
      return true;
    },

    resetRange() {
      this.startOffset = 0;
      this.endOffset = 0;
    },

    addLabel(labelId) {
      if (this.duplicateRange()){
        this.removeLabel(this.duplicateRange());
        const label = {
          start_offset: this.startOffset,
          end_offset: this.endOffset,
          label: labelId,
        };
        this.$emit('add-label', label);
      }
      if (this.validRange()) {
        const label = {
          start_offset: this.startOffset,
          end_offset: this.endOffset,
          label: labelId,
        };
        this.$emit('add-label', label);
      }
    },

    removeLabel(index) {
      this.$emit('remove-label', index);
    },

    makeLabel(startOffset, endOffset) {
      const label = {
        id: 0,
        label: -1,
        start_offset: startOffset,
        end_offset: endOffset,
      };
      return label;
    },

    recommendShortkeyOffset(startOffset, endOffset){
      this.startOffset = startOffset;
      this.endOffset = endOffset;
    },
  },

  watch: {
    entityPositions() {
      this.resetRange();
    },
  },

  computed: {
    sortedEntityPositions() {
      this.entityPositions = this.entityPositions.sort((a, b) => a.start_offset - b.start_offset);
      return this.entityPositions;
    },

    chunks() {
      const res = [];
      let left = 0;
      for (let i = 0; i < this.sortedEntityPositions.length; i++) {
        const e = this.sortedEntityPositions[i];
        const l = this.makeLabel(left, e.start_offset);
        res.push(l);
        res.push(e);
        left = e.end_offset;
      }
      const l = this.makeLabel(left, this.text.length);
      res.push(l);

      return res;
    },

    id2label() {
      let id2label = {};
      // default value;
      id2label[-1] = {
        text_color: '',
        background_color: '',
        text_decoration: '',
      };

      for (let i = 0; i < this.labels.length; i++) {
        const label = this.labels[i];
        label.text_decoration = '';
        id2label[label.id] = label;
      }
      return id2label;
    },
  },
});

Vue.component('recommender', {
  template: '<div><template v-for="r in chunks">\
               <span @click="setSelectedRange(r.start_offset, r.end_offset, id2label[r.label].text_decoration)">\
                 <v-popover style="display: inline" offset="4" v-if="id2label[r.label].text_decoration">\
                          <span class="text-sequence tooltip-target"\
                               v-bind:class="{tag: id2label[r.label].text_color}"\
                               v-bind:style="{textDecoration: id2label[r.label].text_decoration}"\
                          >{{ text.slice(r.start_offset, r.end_offset) }}</span>\
                          <template slot="popover">\
                                <div class="card-header-title has-background-royalblue" style="padding:1.5rem;">\
                                  <div class="field is-grouped is-grouped-multiline">\
                                    <div class="control" v-for="label in labels" v-bind:style="[r.label==label.text ? {\'border\': \'solid red\'} : {\'border\': \'none\'}]">\
                                      <div class="tags has-addons">\
                                        <a class="tag is-medium" v-bind:style="{ color: label.text_color, backgroundColor: label.background_color }"\
                                            v-on:click="annotate(label.id, r.start_offset, r.end_offset)" >{{ label.text }}</a>\
                                        <span class="tag is-medium"><kbd>{{ label.shortcut | simpleShortcut }}</kbd></span>\
                                      </div>\
                                    </div>\
                                  </div>\
                                </div>\
                          </template>\
                        </v-popover>\
                        <span v-else class="text-sequence" \
                        v-bind:class="{tag: id2label[r.label].text_color}"\
                        v-bind:style="{textDecoration: id2label[r.label].text_decoration}">{{ text.slice(r.start_offset, r.end_offset) }}</span>\
                   </span></template></div>',

  props: {
    labels: Array, // [{id: Integer, color: String, text: String}]
    text: String,
    recommendPositions: Array,
  },
  data() {
    return {
      startOffset: 0,
      endOffset: 0,
    };
  },

  methods: {
    setSelectedRange(startoff, endoff, label) {
      if (label == 'underline') {
        this.$parent.recommend_shortkey_offset(startoff, endoff);
        console.log(startoff, endoff);
      }
    },

    makeLabel(startOffset, endOffset) {
      const label = {
        id: 0,
        label: -1,
        start_offset: startOffset,
        end_offset: endOffset,
      };
      return label;
    },

    annotate(labelId, startoff, endoff) {
      console.log(labelId, startoff, endoff);
      this.$parent.recommend_shortkey_offset(startoff, endoff);
      this.$parent.annotate(labelId);
      this.$parent.resetRange();
    },
  },

  computed: {
    sortedRecommendPositions() {
      this.recommendPositions = this.recommendPositions.sort((a, b) => a.start_offset - b.start_offset);
      return this.recommendPositions;
    },

    chunks() {
      const res = [];
      let left = 0;
      for (let i = 0; i < this.sortedRecommendPositions.length; i++) {
        const e = this.sortedRecommendPositions[i];
        const l = this.makeLabel(left, e.start_offset);
        res.push(l);
        res.push(e);
        left = e.end_offset;
      }
      const l = this.makeLabel(left, this.text.length);
      res.push(l);
      console.log(res);
      return res;
    },

    id2label() {
      let id2label = {};
      // default value;
      id2label[-1] = {
        text_decoration: '',
      };

      for (let i = 0; i < this.recommendPositions.length; i++) {
        const label = this.recommendPositions[i].label;
        id2label[label] = {
          text_decoration: 'underline',
        };
      }
      return id2label;
    },
  },
});

const vm = new Vue({
  el: '#mail-app',
  delimiters: ['[[', ']]'],
  components: {
    Loading: Loading,
  },
  mixins: [annotationMixin],
  methods: {
    annotate(labelId) {
      this.$refs.annotator.addLabel(labelId);
    },

    recommend_shortkey_offset(startoff, endoff) {
      this.$refs.annotator.recommendShortkeyOffset(startoff, endoff);
    },

    resetRange() {
      this.$refs.annotator.resetRange();
    },

    addLabel(annotation) {
      const docId = this.docs[this.pageNumber].id;
      HTTP.post(`docs/${docId}/annotations/`, annotation).then((response) => {
        this.annotations[this.pageNumber].push(response.data);
        this.docs[this.pageNumber].annotated = true;
        if (!this.onlineLearningIndices.has(docId)) {
          this.onlineLearningIndices.add(docId);
          this.onlineLearningNum = this.onlineLearningNum + 1;
        }
        HTTP.patch(`docs/${docId}`, {'annotated': true}).then((response) => {
        });
      });
      const history = {
        word: this.$refs.annotator.text.slice(annotation['start_offset'],annotation['end_offset']),
        label: annotation['label']
      };
      HTTP.post(`history/`, history).then((response) => {
        console.log(history);
      });
    },
  },
});