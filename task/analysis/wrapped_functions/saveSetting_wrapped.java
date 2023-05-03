public class SettingsManager {

    public void saveSetting(CustomProperties prop) {
        prop.setProperty("avalanchefever.gametype", mapSet);
        prop.setProperty("avalanchefever.outlinetype", outlinetype);
        prop.setProperty("avalanchefever.numcolors", numColors);
        prop.setProperty("avalanchefever.version", version);
        prop.setProperty("avalanchefever.chainDisplayType", chainDisplayType);
        prop.setProperty("avalanchefever.bigDisplay", bigDisplay);
    }
}