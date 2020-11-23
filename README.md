##Start server

	pip install -r requirements.txt
	pip install flair==0.4.3
	cd alpaca_server
	python -m pip install .
	pip install pyvi
	pip install https://github.com/trungtv/vi_spacy/raw/master/packages/vi_spacy_model-0.2.1/dist/vi_spacy_model-0.2.1.tar.gz
	CUDA_VISIBLE_DEVICES=" " alpaca-serving-start
#start client

	cd ..
	cd alpaca_client
	python -m pip install .
	cd ..
	cd annotation/AlpacaTag/server
	npm install
	npm run build
	cd ..
	python manage.py runserver 0.0.0.0:8000
	
#train

	cd AlpacaTag
	jupyter notebook
#0r	

	python train.py
