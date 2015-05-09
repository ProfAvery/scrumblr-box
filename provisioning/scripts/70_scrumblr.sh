sudo -u vagrant -i npm install -g forever
sudo -u vagrant -i git clone https://github.com/aliasaria/scrumblr.git
sudo -u vagrant -i sh <<EOF
    cd scrumblr
    npm install
    forever start -l forever.log -o out.log -e err.log server.js 8080
EOF
cat >> /etc/rc.local <<EOF
/bin/su - vagrant -c 'cd scrumblr && forever start -l forever.log -o out.log -e err.log -a server.js 8080'
EOF
