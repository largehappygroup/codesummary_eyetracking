public class Encoder {
    
    public String encode( String string ) throws EncoderException {
        byte[] bytes, encoded_bytes;
        String encoded_string = "";
            
        try {
            bytes = string.getBytes( "UTF-8" );
            encoded_bytes = encodeBase64( bytes );
            encoded_string = new String( encoded_bytes );
            
        } catch ( UnsupportedEncodingException ex ) {
            ex.printStackTrace();
        }
        return encoded_string;
    }

    private byte[] encodeBase64( byte[] bytes ) {
        // implementation of Base64 encoding logic
    }
}