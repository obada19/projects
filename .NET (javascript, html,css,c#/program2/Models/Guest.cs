using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;

namespace assignment_3.Models
{
    public class Guest
    {
        public int Id { get; set; }
        
        [Required]
        [StringLength(200)]
        [DisplayName("Name")]
        public string Name { get; set; }
        
        [Required]
        [MaxLength(50), MinLength(5)]
        [DisplayName("Title ")]
        public string Title { get; set; }
        

        [Required]
        [MaxLength(200), MinLength(20)]
        [DisplayName("Message")]
        public string Message { get; set; }
        
    }
}