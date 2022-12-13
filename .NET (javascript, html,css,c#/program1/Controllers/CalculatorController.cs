using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using assignment_2.Models;

namespace assignment_2.Controllers
{
    public class CalculatorController : Controller
    {
        // GET
        public IActionResult Index()
        {
            return View();
        }
    }
}