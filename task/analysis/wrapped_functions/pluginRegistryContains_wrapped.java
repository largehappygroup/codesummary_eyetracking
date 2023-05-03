public class PluginRegistry {

    private List<PluginRegistryNode> registry;

    public PluginRegistry() {
        this.registry = new ArrayList<>();
    }

    public void addNode(PluginRegistryNode node) {
        synchronized (registry) {
            registry.add(node);
        }
    }

    public boolean pluginRegistryContains(String pluginName) {
        synchronized (registry) {
            Iterator<PluginRegistryNode> iter;

            for (iter = registry.iterator(); iter.hasNext(); ) {
                PluginRegistryNode node = iter.next();
                if (node.plugin.getName().equals(pluginName)) {
                    return true;
                }
            }
        }
        return false;
    }

}