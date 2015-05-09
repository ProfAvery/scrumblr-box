apt-get -y install redis-server
npm install -g redis-dump
echo >> $HOME/.bashrc << EOF
    alias dump='redis-dump > $HOME/shared/redis-dump.$(perl -e "print time, \"\n\"")'
EOF

