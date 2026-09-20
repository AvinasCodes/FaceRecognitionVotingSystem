from twilio.rest import Client
import os
from dotenv import load_dotenv

def test_twilio_otp():
    # Load environment variables
    load_dotenv()

    # Twilio credentials from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    verify_service_sid = os.getenv('TWILIO_VERIFY_SERVICE_SID')

    if not all([account_sid, auth_token, verify_service_sid]):
        print("Error: Missing TWILIO environment variables in .env file.")
        return

    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Test mobile number from environment variable or prompt
        test_number = os.getenv('TEST_PHONE_NUMBER')
        if not test_number:
            test_number = input("Enter test mobile number (with country code, e.g. +91XXXXXXXXXX): ").strip()
        
        print("1. Testing OTP sending...")
        
        # Send verification code
        verification = client.verify \
            .v2 \
            .services(verify_service_sid) \
            .verifications \
            .create(to=test_number, channel='sms')
            
        print(f"Verification status: {verification.status}")
        
        if verification.status == 'pending':
            # Get OTP input from user
            otp_code = input("Enter the OTP received: ")
            
            print("\n2. Testing OTP verification...")
            
            # Verify the code
            verification_check = client.verify \
                .v2 \
                .services(verify_service_sid) \
                .verification_checks \
                .create(to=test_number, code=otp_code)
                
            print(f"Verification check status: {verification_check.status}")
            
            if verification_check.status == 'approved':
                print("\n✅ OTP Test Successful!")
                print("Both sending and verification working correctly.")
            else:
                print("\n❌ OTP Verification Failed!")
                print(f"Status: {verification_check.status}")
        else:
            print("\n❌ OTP Sending Failed!")
            print(f"Status: {verification.status}")
            
    except Exception as e:
        print("\n❌ Test Failed with error:")
        print(str(e))

if __name__ == "__main__":
    print("Starting Twilio OTP Test...\n")
    test_twilio_otp()