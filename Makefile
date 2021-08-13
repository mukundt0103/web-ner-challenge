default:
	@echo "An explicit target is required"

install:
	cd $(FRONTEND) && npm install
	cd $(BACKEND) && pip3 install -r requirements.txt

start:
	cd $(FRONTEND) && npm run serve &
	cd $(BACKEND) && flask run
