public class CountryTest {
    
    public void testAddCountryWithSequenceGenerator() throws Exception {
        CountryWithSequence country1 = new CountryWithSequence();
        country1.setCountryId( "KR" );
        country1.setCountryName( "Korea" );

        Integer countryCode = ( Integer ) session.save( country1 );
        assertEquals( "fail to generate a new countryCode.", 0, countryCode.intValue() );
        assertNotNull( "fail to add a new country with sequence generator.", countryCode );
    }
}