from google.cloud import storage

def image_upload_to_gcs(bucket_name, file, filename):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_file(file)