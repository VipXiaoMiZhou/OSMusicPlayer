import hashlib

class Tool:

    @staticmethod
    def encrypted_id(id):
        byte1 = bytearray('3go8&$8*3*3h0k(2)2')
        byte2 = bytearray(id)
        byte1_len = len(byte1)
        for i in range(len(byte2)):
            byte2[i] = byte2[i]^byte1[i%byte1_len]
        m = hashlib.md5()
        m.update(byte2)
        result = m.digest().encode('base64')[:-1]
        result = result.replace('/', '_')
        result = result.replace('+', '-')
        return result

encrypted_id = Tool.encrypted_id('5768037999439349')
print(encrypted_id)