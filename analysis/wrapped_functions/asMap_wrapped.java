public class MapConverter {
    public Map asMap() {
        Map map = new HashMap();
        // map.put ( "org_id", org_id );
        map.put( "startDate", start_date );
        map.put( "endDate", end_date );

        if ( this.organization != null )
            map.put( "organization", this.organization.acronym );
        map.put( "type", ( this.isVisitor() ? "Visitor" : "Employee" ));
        // return new JSONObject( map );
        return map;
    }
}