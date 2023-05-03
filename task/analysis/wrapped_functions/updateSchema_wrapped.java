```java
public class SchemaUpdater {

    public void updateSchema( String kind, SchemaTO schemaTO ) {
        try {
            restTemplate.postForObject( baseURL + "schema/" + kind + "/update", schemaTO, SchemaTO.class );
        } catch ( SyncopeClientCompositeErrorException e ) {
            LOG.error( "While updating a user schema", e );
        }
    }

}
```