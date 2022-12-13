using System.Linq;
using assignment_3.Data;
using assignment_3.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace assignment_3.Controllers
{
    public class GuestbookController : Controller
    {
        private readonly ILogger<GuestbookController> _logger;
        private readonly ApplicationDbContext _db;
        public GuestbookController(ILogger<GuestbookController> logger, ApplicationDbContext db)
        {
            _logger = logger;
            _db = db;
        }
        public IActionResult Index()
        {
            _logger.LogDebug(" fetching guests list");
            return View(_db.Guests.ToList());
        }
        [HttpGet]
        public IActionResult Add()
        {
            return View(new Guest());
        }
        [HttpPost]
        public IActionResult Add(Guest guest)
        {
            _logger.LogDebug("posting a new guest in the book");

            if (!ModelState.IsValid)
            {
                _logger.LogWarning("you have entered something wrong please check again");
                return View(guest);
            }

            _db.Guests.Add(guest);
            _db.SaveChanges();
            return RedirectToAction(nameof(Index));
        }

    }
}