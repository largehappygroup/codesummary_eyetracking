public class GraphCreator {
    private int num_models;
    private Community community;

    public GraphCreator(Community community) {
        this.num_models = 0;
        this.community = community;
    }

    public GraphModel createGraphModel(List includedNodes) {
        num_models++;
        System.out.println("PGraphModel: creating a new non-super graphmodel: " + num_models);

        GraphModel model = new PGraphModel("Phoebe" + num_models, getModelSubSet(includedNodes));
        community.add(model);

        return model;
    }

    private List getModelSubSet(List includedNodes) {
        // implementation omitted for brevity
    }
}