import os

def create_drive_folder(gmail, folder_name, credentials_file=None):
    """Create a folder in Google Drive for the specified Gmail account"""
    try:
        from google.oauth2.credentials import Credentials  # type: ignore
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
        from googleapiclient.errors import HttpError  # type: ignore
    except ImportError as e:
        raise ImportError(
            "Google API libraries are not installed. Install them using: "
            "pip install google-api-python-client google-auth-oauthlib"
        ) from e

    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    
    creds_path = credentials_file or os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Google credentials file not found: {creds_path}")

    try:
        # Initialize the Drive API client
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)
        
        service = build('drive', 'v3', credentials=creds)
        
        # Create folder metadata
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        
        # Create the folder
        folder = service.files().create(
            body=folder_metadata,
            fields='id'
        ).execute()
        
        return folder.get('id')
        
    except HttpError as error:
        print(f'An error occurred: {error}')
        raise error