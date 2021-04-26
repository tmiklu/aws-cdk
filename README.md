
# Welcome to your CDK Python project!

sudo apt-get install python3-venv 
sudo apt-get install npm 
sudo npm install -g aws-cdk 

AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXX 
AWS_ACCESS_KEY_ID=YYYYYYYYYYYYYYYYY 

cdk init --language python 

#### 
python -m venv .venv 
source .venv/bin/activate 
pip install -r requirement.txt 
pip install aws-cdk.aws_ec2 
pip install aws_cdk.aws_ecs 

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
