public class LockedFileLoader {
    
    private void load( LockedFile file ) throws SQLIOException {
        file.setPosition( POS_HEADER );
    
        byte[] buffer = new byte[ BASE_HEADER_SIZE ];
        file.read( buffer, 0, BASE_HEADER_SIZE );
    
        type = buffer[ POS_TYPE ];
        lastUpdate = decode3Date( buffer, POS_LAST_UDPATE );
        recordsNum = DbfUtils.decodeLittleUint16( buffer, POS_RECORDS_NUM );
        recordSize = DbfUtils.decodeLittleUint16( buffer, POS_RECORD_SIZE );
        headerSize = DbfUtils.decodeLittleUint16( buffer, POS_HEADER_SIZE );
    
        verifyAndFixHeader( file );
    } 

}