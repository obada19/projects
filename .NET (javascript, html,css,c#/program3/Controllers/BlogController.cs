using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using assignment_4.Data;
using assignment_4.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;


namespace assignment_4.Controllers
{
    [Authorize]
    public class BlogController : Controller
    {
        
        private readonly ApplicationDbContext _context;
        private readonly UserManager<ApplicationUser> _um;

        public BlogController(ApplicationDbContext context, UserManager<ApplicationUser> um)
        {
            _um = um;
            _context = context;
        }
        
        // GET: posts
        [AllowAnonymous]
        public IActionResult Index()
        {
            var vm = new ViewModelPost
            {
                Post = new Post(),
                Posts = _context.Posts.Include(u=>u.ApplicationUser).OrderByDescending(o => o.Id).ToListAsync().Result
            };
            return View(vm);
            
        }
        

        // GET: add post
      
        public IActionResult Add()
        {
            return View();
        }
 
        
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Add([Bind("Id,Title,Summary,Content")] Post post)
        {
            if (ModelState.IsValid)
            {
                post.Time = DateTime.Now;
                post.ApplicationUser = _um.GetUserAsync(User).Result;
                _context.Add(post);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(post);
        }

        // GET: posts Edit/5
        public IActionResult Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }
           
            var post = _context.Posts.First(p => p.Id == id && p.ApplicationUserId ==  _um.GetUserId(User) );
            if (post == null)
            {
                return NotFound();
            }
            
            return View(post);
        }

        // POST: A/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Summary,Content")] Post post)
        {
            if (id != post.Id)
            {
                return NotFound();
            }
            var po = _context.Posts.First(p => p.Id == id && p.ApplicationUserId ==  _um.GetUserId(User) );
            
            if (po == null)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    post.Time = DateTime.Now;
                    post.ApplicationUser = _um.GetUserAsync(User).Result;
                    _context.Update(post);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!PostExists(post.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(post);
        }
        


        private bool PostExists(int id)
        {
            return _context.Posts.Any(e => e.Id == id);
        }
    }
}
