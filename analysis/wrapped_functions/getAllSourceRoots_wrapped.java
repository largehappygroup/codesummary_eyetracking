public class MyClass {

    public Set getAllSourceRoots(String pluginName, Version pluginVersion) {
        Set pluginSourceRoots = new HashSet();
        ManifestElement[] manifestElements = getSourceEntries(pluginName, pluginVersion);

        if (manifestElements != null) {
            for (int j = 0; j < manifestElements.length; j++) {
                ManifestElement currentElement = manifestElements[j];
                addSourceRoots(currentElement.getDirective("roots"), pluginSourceRoots); //$NON-NLS-1$
            }
        }
        return pluginSourceRoots;
    }

    private void addSourceRoots(String directive, Set pluginSourceRoots) {
        // implementation omitted
    }

    private ManifestElement[] getSourceEntries(String pluginName, Version pluginVersion) {
        // implementation omitted
    }
}