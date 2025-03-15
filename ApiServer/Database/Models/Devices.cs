using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ApiServer.Database.Models
{
    public class Devices
    {

        [Key, DatabaseGenerated(DatabaseGeneratedOption.Identity), Required]
        public Guid deviceGuid { get; set; }
        public string DisplayName { get; set; }
        public string DisplayLocation { get; set; }
        public int CurrentDeviceAmount { get; set; }

    }
}
