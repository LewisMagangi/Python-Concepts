import uuid

def display_uuid_examples():
    # Make a UUID based on the host ID and current time
    uuid1_example = uuid.uuid1()
    print("UUID based on host ID and current time (uuid1):", uuid1_example)
    
    # Make a UUID using an MD5 hash of a namespace UUID and a name
    uuid3_example = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    print("UUID using MD5 hash of a namespace UUID and a name (uuid3):", uuid3_example)
    
    # Make a random UUID
    uuid4_example = uuid.uuid4()
    print("Random UUID (uuid4):", uuid4_example)
    
    # Make a UUID using a SHA-1 hash of a namespace UUID and a name
    uuid5_example = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    print("UUID using SHA-1 hash of a namespace UUID and a name (uuid5):", uuid5_example)
    
    # Make a UUID from a string of hex digits (braces and hyphens ignored)
    example_string = '{00010203-0405-0607-0809-0a0b0c0d0e0f}'
    uuid_from_string = uuid.UUID(example_string)
    print("UUID from a string of hex digits:", uuid_from_string)
    
    # Convert a UUID to a string of hex digits in standard form
    uuid_as_string = str(uuid_from_string)
    print("UUID as a string in standard form:", uuid_as_string)
    
    # Get the raw 16 bytes of the UUID
    uuid_bytes = uuid_from_string.bytes
    print("Raw 16 bytes of the UUID:", uuid_bytes)
                                                                                
    # Make a UUID from a 16-byte string
    uuid_from_bytes = uuid.UUID(bytes=uuid_bytes)
    print("UUID from a 16-byte string:", uuid_from_bytes)

if __name__ == "__main__":
    display_uuid_examples()
                                                                                                            
