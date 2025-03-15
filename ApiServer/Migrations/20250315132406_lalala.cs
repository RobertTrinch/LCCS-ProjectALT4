using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ApiServer.Migrations
{
    /// <inheritdoc />
    public partial class lalala : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "time",
                table: "Movements",
                newName: "movementTime");

            migrationBuilder.RenameColumn(
                name: "CurrentAmount",
                table: "Devices",
                newName: "CurrentDeviceAmount");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "movementTime",
                table: "Movements",
                newName: "time");

            migrationBuilder.RenameColumn(
                name: "CurrentDeviceAmount",
                table: "Devices",
                newName: "CurrentAmount");
        }
    }
}
