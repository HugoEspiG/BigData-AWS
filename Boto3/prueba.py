import boto3

# Crear un cliente de S3 sin especificar credenciales (usará las de la instancia)
s3_client = boto3.client('s3')

# Listar los nombres de los buckets
def listar_buckets():
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets

# Listar todos los archivos de un bucket
def listar_archivos(bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    archivos = [obj['Key'] for obj in response.get('Contents',[])]
    return archivos

# Subir un archivo a un bucket
def subir_archivo(bucket_name, file_path, object_name):
    s3_client.upload_file(file_path, bucket_name, object_name)

# Descargar un archivo de un bucket
def descargar_archivo(bucket_name, object_name, destination_path):
    s3_client.download_file(bucket_name, object_name, destination_path)

if __name__ == '__main__':
    # Cambiar por los nombres de tus buckets y archivos
    bucket_1 = 'bigdata2023hugoespinosa'
    bucket_2 = 'buckethugoa'
    archivo_subir = 'archivo.txt'
    archivo_descargar = 'archivo.txt'

    print("Nombres de los buckets:")
    print(listar_buckets())


    print(f"Archivos en el {bucket_1}:")
    print(listar_archivos(bucket_1))

    print(f"Archivos en el {bucket_2}:")
    print(listar_archivos(bucket_2))

    print(f"Subiendo archivo al {bucket_1}...")
    subir_archivo(bucket_1,archivo_subir, archivo_subir)

    print(f"Descargando archivo del {bucket_1}...")
    descargar_archivo(bucket_1, archivo_descargar, f'descargado_{archivo_descargar}')