using System.Collections.Generic;

namespace assignment_4.Models
{
    public class ViewModelPost
    {
        public Post Post { get; set; }
        public IEnumerable<Post> Posts { get; set; }

        public ViewModelPost()
        {
            Posts = new List<Post>();
        }
    }
}