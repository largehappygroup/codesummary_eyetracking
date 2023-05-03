Unfortunately, as an AI language model, I am not able to create files. However, I can provide you with the class structure you can use to wrap your function:

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

Make sure to import the necessary libraries and instantiate the InputField object in your code.