using ApiServer.Database.Models;
using Microsoft.EntityFrameworkCore;

namespace ApiServer.Database
{
    public class DatabaseContext : DbContext
    {

        public DbSet<Devices> Devices { get; set; }
        public DbSet<Movements> Movements { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            //optionsBuilder.UseSqlite($"Data Source=C:\\Users\\Robert\\source\\repos\\TrinchPhotosWebsite\\TrinchPhotos-Web\\bin\\Debug\\net8.0\\TrinchPhotosWeb.db");
            optionsBuilder.UseNpgsql("aaaa");
        }

    }
}
