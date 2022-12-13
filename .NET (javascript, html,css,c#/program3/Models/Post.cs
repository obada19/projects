using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Identity;

namespace assignment_4.Models
{
    public class Post
    {
        public int Id { get; set; }
        
        [Required]
        [StringLength(100)]
        [DisplayName("Title")]
        public string Title { get; set; }

        [Required]
        [StringLength(500)]
        [DisplayName("Summary")]
        public string Summary { get; set; }
        
        [Required]
        [StringLength(10000)]
        [DisplayName("Content")]
        public string Content { get; set; }
        
        [DataType(DataType.DateTime)]
        [DisplayName("Time")]
        public DateTime Time { get; set; }
        
        
        public string ApplicationUserId { get; set; }
        public ApplicationUser ApplicationUser { get; set; }
    }
}