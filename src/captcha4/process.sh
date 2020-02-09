rm -rf ./backend && cp -r ../captcha1/backend .
rm -rf ./frontend && cp -r ../captcha1/frontend .
rm -rf ./frontend/node_modules
echo "Copied Folder"
cat ./frontend/nginx.conf | sed 's/captcha1/captcha4/g' > ./frontend/nginx.conf.bak && mv ./frontend/nginx.conf.bak ./frontend/nginx.conf
echo "Repalced nginx.conf"
