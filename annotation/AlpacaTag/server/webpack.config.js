const process = require('process');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    mode: process.env.DEBUG === 'False' ? 'production' : 'development',
    entry: {
        'sequence_labeling': './static/js/sequence_labeling.js',
        'projects': './static/js/projects.js',
        'stats': './static/js/stats.js',
        'label': './static/js/label.js',
        'setting': './static/js/setting.js',
        'upload': './static/js/upload.js',
        'dictionary': './static/js/dictionary.js'
    },
    output: {
        path: __dirname + '/static/bundle',
        filename: '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
              test: /\.css$/,
              include: /node_modules/,
              loaders: ['style-loader', 'css-loader'],
             }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            vue$: 'vue/dist/vue.esm.js',
        },
    },
}