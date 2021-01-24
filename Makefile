run:
	@echo "Build knn with iris"
	@python3 build_model.py
	@echo "Start web server, try curl http://127.0.0.1:5000/predictions or use the frontend.html"
	@python3 app.py