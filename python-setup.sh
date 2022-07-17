#!/bin/bash

package_check () {   
   if ! which $1;
   then
    echo "The $1 is not installed."
    apt update -y
    apt install "$1" -y
    echo "The $1 is now installed."
   else
    echo "The $1 is already installed."
   fi 
}

package_check python3
package_check pip

pip install boto3
pip install aws-sdk-s3