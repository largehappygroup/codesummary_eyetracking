public class MyClass {
    
    public List getStatusFlagFields() {
        List list = new ArrayList();
        String statusFlagPath = "/collectionConfigRecord/statusFlags/statusFlag/status";
        for ( Iterator i = im.getInputFields().iterator(); i.hasNext(); ) {
            InputField field = ( InputField ) i.next();
            // prtln ( field.toString() );
            if ( field.getNormalizedXPath().startsWith( statusFlagPath )) {
                list.add( field );
            }
        }
        return list;
    }
} 