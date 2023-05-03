public class TemplateResolver {
    protected String resolveValue(MagnetContext aContext, String aValue) throws RenderingException {
        try {
            if (aValue == null) {
                return null;
            } else {
                TemplateElementIF aTemplate = _theTemplateFactory.parse(aValue);
                return aTemplate.render(aContext);
            }
        } catch (TemplateException te) {
            throw new RenderingException("Unable to resolve the value " + aValue, te);
        }
    }
}