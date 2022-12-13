using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using assignment_3.Models;
using Microsoft.EntityFrameworkCore;

namespace assignment_3.Data
{
    public class ApplicationDbInitializer
    {
        public static void Initialize(ApplicationDbContext db)
        {
            db.Database.EnsureDeleted();
            db.Database.EnsureCreated();

            for (int i = 1; i <= 5; i++)
            {
                db.Guests.Add(new Guest
                {
                    Name = $"name { i }",
                    Title = $"title{ i }",
                    Message = $"message{ i }"
                });
            }

            db.SaveChanges();
        }
    }
}