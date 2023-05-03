```java
public class SqlGenerator {
    public void genSql() throws PositionedError {
        try {
            SqlcPrettyPrinter spp;
            spp = new SqlcPrettyPrinter( ref.getFile() );
            spp.printCUnit( elems );
            spp.close();
        } catch ( IOException ioe ) {
            ioe.printStackTrace();
            System.err.println( "cannot write: " + ref.getFile() );
        }
    }
}
```