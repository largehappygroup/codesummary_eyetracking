public class MyClass {
   public void testOneTwoThreeCreateCycle() throws Exception {
      IRodinFile ctx = createRodinFile("P/x.ctx");
      createDependency(ctx, "y");
      createData(ctx, "one");
      ctx.save(null, true);
      runBuilder();

      IRodinFile cty = createRodinFile("P/y.ctx");
      createDependency(cty, "x");
      createData(cty, "two");
      cty.save(null, true);

      IRodinFile ctz = createRodinFile("P/z.ctx");
      createData(ctz, "three");
      ctz.save(null, true);

      runBuilder("CSC extract /P/x.ctx", "CSC run /P/x.csc", "CSC extract /P/y.ctx",
            "CSC extract /P/z.ctx", "CSC run /P/z.csc");
   }
}