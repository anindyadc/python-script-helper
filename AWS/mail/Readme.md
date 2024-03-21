# Obtaining Amazon SES SMTP credentials

Reference:
https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html

The following pseudocode shows the algorithm that converts an AWS secret access key to an SES SMTP password.
```
// Modify this variable to include your AWS secret access key
key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
            
// Modify this variable to refer to the AWS Region that you want to use to send email.
region = "us-west-2";
            
// The values of the following variables should always stay the same.
date = "11111111";
service = "ses";
terminal = "aws4_request";
message = "SendRawEmail";
version = 0x04;

kDate = HmacSha256(date, "AWS4" + key);
kRegion = HmacSha256(region, kDate);
kService = HmacSha256(service, kRegion);
kTerminal = HmacSha256(terminal, kService);
kMessage = HmacSha256(message, kTerminal);
signatureAndVersion = Concatenate(version, kMessage);
smtpPassword = Base64(signatureAndVersion);
```
To obtain your SMTP password by using this script, save the preceding code as `smtp_credentials_generate.py`  Then, at the command line, run the following command:
```
python path/to/smtp_credentials_generate.py wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY us-east-1
```

In the preceding command, do the following:

Replace path/to/ with the path to the location where you saved smtp_credentials_generate.py.

Replace wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY with the secret access key that you want to convert into an SMTP password.

Replace us-east-1 with the AWS Region in which you want to use the SMTP credentials.

When this script runs successfully, the only output is your SMTP password.
