import java.util.Iterator;

public class MyClass {
    // Assuming registry is a collection of PluginRegistryNode
    Iterable<PluginRegistryNode> registry;

    public boolean pluginRegistryContains(String pluginName) {
        synchronized (registry) {
            Iterator iter;

            for (iter = registry.iterator(); iter.hasNext(); ) {
                PluginRegistryNode node = (PluginRegistryNode) iter.next();
                if (node.plugin.getName().equals(pluginName)) return true;
            }
        }
        return false;
    }

    // Placeholder class definitions, replace these with your actual class definitions
    class PluginRegistryNode {
        // Your PluginRegistryNode class implementation goes here
        Plugin plugin;
    }

    class Plugin {
        // Your Plugin class implementation goes here
        String getName() {
            // Replace this with your actual implementation
            return "";
        }
    }
}