import os
import subprocess
import pickle
import hashlib
import http.server
import socketserver
import ssl
import json

# Hardcoded credentials (secrets in code)
API_KEY = "12345-ABCDE-SECRET"
DB_USER = "admin"
DB_PASS = "password123"

# Hardcoded AWS credentials (EXTREMELY INSECURE)
AWS_ACCESS_KEY = "AKIAEXAMPLEKEY"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def insecure_hash(data):
    # Weak hashing algorithm
    return hashlib.md5(data.encode()).hexdigest()

def insecure_eval(user_input):
    # Arbitrary code execution
    return eval(user_input)

def insecure_system(user_input):
    # Command injection vulnerability
    os.system("echo " + user_input)

def insecure_subprocess(user_input):
    # Command injection via shell=True
    return subprocess.check_output("ls " + user_input, shell=True)

def insecure_deserialization(payload):
    # Insecure deserialization (pickle.loads)
    return pickle.loads(payload)

def insecure_sql(user_input):
    # SQL injection via string concatenation
    query = "SELECT * FROM users WHERE name = '" + user_input + "';"
    print("Executing query:", query)
    return query

def insecure_aws_call():
    # Using AWS CLI with hardcoded credentials passed on command line (logs attackers can see)
    cmd = (
        f"AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY} "
        f"AWS_SECRET_ACCESS_KEY={AWS_SECRET_KEY} "
        "aws s3 cp somefile s3://insecure-bucket --acl public-read"
    )
    os.system(cmd)  # exposes credentials and can be shell-injected

def write_cloudformation_template():
    # Write intentionally insecure CloudFormation to file
    cf = INSECURE_CF_TEMPLATE
    with open("insecure-stack.yaml", "w") as f:
        f.write(cf)

def main():
    print("=== Insecure DevOps + IaC Demo ===")
    print("Weak hash:", insecure_hash("secret"))
    try:
        insecure_eval("__import__('os').system('echo hello')")
    except Exception:
        pass
    insecure_system("; echo vulnerable")
    insecure_subprocess("; cat /etc/passwd")
    insecure_sql("admin' OR '1'='1")
    payload = pickle.dumps(lambda: os.system("echo pickled"))
    insecure_deserialization(payload)
    write_cloudformation_template()
    insecure_aws_call()
    print("Wrote insecure CloudFormation template to insecure-stack.yaml")
