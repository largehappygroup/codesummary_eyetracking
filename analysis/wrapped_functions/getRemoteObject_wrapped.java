public class MyClass {
    public DBusInterface getRemoteObject( String objectpath ) throws DBusException {
        if ( null == objectpath ) { 
            throw new DBusException(_( "Invalid object path: null" )); 
        }
        if ( !objectpath.matches( OBJECT_REGEX )||( objectpath.length() > MAX_NAME_LENGTH )){
            throw new DBusException(( "Invalid object path: " ) + objectpath); 
        }
        return dynamicProxy( objectpath );
    }
}