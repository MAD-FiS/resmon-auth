#!/bin/bash

echo "ResMon builder"
echo "----------------------"
echo ""

rm -f `find -name '*.pyc'`
rm -rf `find -name  '__pycache__'`

cat ./scripts/install.template > install-auth.sh
echo "ARCHIVE_DATA:" >> install-auth.sh
echo "- Install file is created"

tar -czvf tmp.tar.gz src resmon-auth secret.key README.md requirements resmon-auth.env >> /dev/null
cat tmp.tar.gz >> install-auth.sh
rm tmp.tar.gz
echo "- Required data is compressed and included"

chmod 770 install-auth.sh
echo "- File ./install-auth.sh is ready to be used"
