using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(GratefulHearts.Startup))]
namespace GratefulHearts
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
