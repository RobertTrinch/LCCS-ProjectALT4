using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ApiServer.Database.Models
{
    public class Movements
    {

        [Key, DatabaseGenerated(DatabaseGeneratedOption.Identity), Required]
        public Guid movementGuid { get; set; }
        public Guid Device { get; set; }
        public DateTime movementTime { get; set; }
        public bool Entry { get; set; } // true = entered, false = exit

    }
}
