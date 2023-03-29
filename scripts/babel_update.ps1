#!/bin/sh

CURRENT_DIR="$( cd "$( dirname "%~dp0" )" && pwd )"
ROOT_DIR="$( cd "$( dirname "%~dp0" )" && cd .. && pwd )"
LICENSE_TMP=$(date /t | tr ' ' '_')

echo "# Licensed to the Apache Software Foundation (ASF) under one" > %LICENSE_TMP%
echo "# or more contributor license agreements.  See the NOTICE file" >> %LICENSE_TMP%
echo "# distributed with this work for additional information" >> %LICENSE_TMP%
echo "# regarding copyright ownership.  The ASF licenses this file" >> %LICENSE_TMP%
echo "# to you under the Apache License, Version 2.0 (the" >> %LICENSE_TMP%
echo "# \"License\"); you may not use this file except in compliance" >> %LICENSE_TMP%
echo "# with the License.  You may obtain a copy of the License at" >> %LICENSE_TMP%
echo "#" >> %LICENSE_TMP%
echo "#   http://www.apache.org/licenses/LICENSE-2.0" >> %LICENSE_TMP%
echo "#" >> %LICENSE_TMP%
echo "# Unless required by applicable law or agreed to in writing," >> %LICENSE_TMP%
echo "# software distributed under the License is distributed on an" >> %LICENSE_TMP%
echo "# \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY" >> %LICENSE_TMP%
echo "# KIND, either express or implied.  See the License for the" >> %LICENSE_TMP%
echo "# specific language governing permissions and limitations" >> %LICENSE_TMP%
echo "# under the License." >> %LICENSE_TMP%

cd %ROOT_DIR%
pybabel extract -F superset\translations\babel.cfg -o superset\translations\messages.pot --sort-output --copyright-holder=Superset --project=Superset -k _ -k __ -k t -k tn -k tct .

type %LICENSE_TMP% superset\translations\messages.pot > messages.pot.tmp \
  && move /Y messages.pot.tmp superset\translations\messages.pot

pybabel update -i superset\translations\messages.pot -d superset\translations --ignore-obsolete

cd %CURRENT_DIR%
