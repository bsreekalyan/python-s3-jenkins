#!/bin/bash

package_check () {   
   if ! which $1;
   then
    echo "The $1 is not installed."
    apt update -y
    apt install "$1" -y
   else
    echo "The $1 is already installed."
   fi 
}

package_check python3
package_check pip

pip install boto3