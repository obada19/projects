using System;
using Microsoft.AspNetCore.Identity;

using assignment_4.Models;
using Microsoft.Extensions.DependencyInjection;

namespace assignment_4.Data
{
    public static class ApplicationDbInitializer
    {

        public static void Initialize(IServiceProvider services)
        {

            var db = services.GetRequiredService<ApplicationDbContext>();


            db.Database.EnsureDeleted();
            db.Database.EnsureCreated();


            var um = services.GetRequiredService<UserManager<ApplicationUser>>();
            var rm = services.GetRequiredService<RoleManager<IdentityRole>>();

            /*
            // Create the admin role
            var adminRole = new IdentityRole("Admin");

            // Add the admin role
            rm.CreateAsync(adminRole).Wait();
            */

            // Add a regular user (no extra roles)
           // var user = InitUsersApplicationUser(um);

            /*
           
            // Add an admin user (in the admin role)
            var admin = new ApplicationUser
            {
                UserName = "admin@uia.no",
                Email = "admin@uia.no",
                Nickname = "knutinne",
                EmailConfirmed = true
            };

            um.CreateAsync(admin, "Password1.").Wait();
            um.AddToRoleAsync(admin, adminRole.Name).Wait();
            */
        
             
            // Add 5 posts
    
            db.SaveChanges();
        }

        private static ApplicationUser InitUsersApplicationUser(UserManager<ApplicationUser> um)
        {
            
            var user = new ApplicationUser
            {
                UserName = "user@uia.no",
                Email = "user@uia.no",
                Nickname = "knut",
                EmailConfirmed = true
            };
            um.CreateAsync(user, "Password1.").Wait();
            return user;
        }
    }
}