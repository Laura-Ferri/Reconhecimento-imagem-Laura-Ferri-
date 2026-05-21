// ──────────────────────────────────────────────
// CONSTANTS & STATE
// ──────────────────────────────────────────────

const STORAGE_KEYS = {
  users: 'todo_users',
  todos: 'todos',
  session: 'todo_session',
};

// ──────────────────────────────────────────────
// STORAGE HELPERS
// ──────────────────────────────────────────────

function getUsers() {
  return JSON.parse(localStorage.getItem(STORAGE_KEYS.users) || '[]');
}

function saveUsers(users) {
  localStorage.setItem(STORAGE_KEYS.users, JSON.stringify(users));
}

function getTodos() {
  return JSON.parse(localStorage.getItem(STORAGE_KEYS.todos) || '[]');
}

function saveTodos(todos) {
  localStorage.setItem(STORAGE_KEYS.todos, JSON.stringify(todos));
}

function getSession() {
  return JSON.parse(localStorage.getItem(STORAGE_KEYS.session) || 'null');
}

function saveSession(user) {
  localStorage.setItem(STORAGE_KEYS.session, JSON.stringify(user));
}

function clearSession() {
  localStorage.removeItem(STORAGE_KEYS.session);
}

// ──────────────────────────────────────────────
// SCREEN MANAGEMENT
// ──────────────────────────────────────────────

function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + id).classList.add('active');
}

// ──────────────────────────────────────────────
// TAB SWITCHING (Login / Register)
// ──────────────────────────────────────────────

function switchTab(tab) {
  const loginForm = document.getElementById('form-login');
  const registerForm = document.getElementById('form-register');
  const tabLogin = document.getElementById('tab-login');
  const tabRegister = document.getElementById('tab-register');

  if (tab === 'login') {
    loginForm.classList.remove('hidden');
    registerForm.classList.add('hidden');
    tabLogin.classList.add('active-tab');
    tabRegister.classList.remove('active-tab');
    tabLogin.classList.replace('text-slate-400', 'text-slate-300');
    tabRegister.classList.replace('text-slate-300', 'text-slate-400');
  } else {
    registerForm.classList.remove('hidden');
    loginForm.classList.add('hidden');
    tabRegister.classList.add('active-tab');
    tabLogin.classList.remove('active-tab');
    tabRegister.classList.replace('text-slate-400', 'text-slate-300');
    tabLogin.classList.replace('text-slate-300', 'text-slate-400');
  }

  hideAlert('login-alert');
  hideAlert('register-alert');
}

// ──────────────────────────────────────────────
// ALERT HELPERS
// ──────────────────────────────────────────────

function showAlert(id, message, type) {
  const el = document.getElementById(id);
  el.textContent = message;
  el.className = 'alert-msg ' + (type === 'success' ? 'alert-success' : 'alert-error');
  el.style.display = 'block';
}

function hideAlert(id) {
  const el = document.getElementById(id);
  if (el) el.style.display = 'none';
}

// ──────────────────────────────────────────────
// AUTH HANDLERS
// ──────────────────────────────────────────────

function handleRegister(event) {
  event.preventDefault();

  const name = document.getElementById('register-name').value.trim();
  const email = document.getElementById('register-email').value.trim().toLowerCase();
  const password = document.getElementById('register-password').value;

  const users = getUsers();
  const exists = users.find(u => u.email === email);

  if (exists) {
    showAlert('register-alert', 'Este e-mail ja esta cadastrado. Faca login.', 'error');
    return;
  }

  const newUser = { name, email, password };
  users.push(newUser);
  saveUsers(users);

  showAlert('register-alert', 'Conta criada com sucesso! Faca login.', 'success');
  document.getElementById('form-register').reset();

  setTimeout(() => switchTab('login'), 1500);
}

function handleLogin(event) {
  event.preventDefault();

  const email = document.getElementById('login-email').value.trim().toLowerCase();
  const password = document.getElementById('login-password').value;

  const users = getUsers();
  const user = users.find(u => u.email === email && u.password === password);

  if (!user) {
    showAlert('login-alert', 'E-mail ou senha incorretos.', 'error');
    return;
  }

  saveSession(user);
  loadDashboard(user);
}

function handleLogout() {
  clearSession();
  document.getElementById('form-login').reset();
  document.getElementById('form-task').reset();
  switchTab('login');
  showScreen('auth');
}

// ──────────────────────────────────────────────
// DASHBOARD
// ──────────────────────────────────────────────

function loadDashboard(user) {
  document.getElementById('greeting').textContent = 'Ola, ' + user.name;
  showScreen('dashboard');
  renderTasks(user.email);
}

// ──────────────────────────────────────────────
// TASK HANDLERS
// ──────────────────────────────────────────────

function handleAddTask(event) {
  event.preventDefault();

  const session = getSession();
  if (!session) return;

  const title = document.getElementById('task-title').value.trim();
  const type = document.getElementById('task-type').value;
  const description = document.getElementById('task-desc').value.trim();

  if (!title) return;

  const newTask = {
    id: Date.now(),
    userId: session.email,
    title,
    type,
    description,
    done: false,
  };

  const todos = getTodos();
  todos.push(newTask);
  saveTodos(todos);

  document.getElementById('form-task').reset();
  renderTasks(session.email);
}

function handleToggleDone(taskId) {
  const todos = getTodos();
  const task = todos.find(t => t.id === taskId);
  if (task) {
    task.done = !task.done;
    saveTodos(todos);
    renderTasks(getSession().email);
  }
}

function handleDeleteTask(taskId) {
  const todos = getTodos().filter(t => t.id !== taskId);
  saveTodos(todos);
  renderTasks(getSession().email);
}

// ──────────────────────────────────────────────
// RENDER TASKS
// ──────────────────────────────────────────────

function getBadgeClass(type) {
  const map = {
    Trabalho: 'badge-trabalho',
    Pessoal: 'badge-pessoal',
    Estudos: 'badge-estudos',
  };
  return map[type] || 'badge-pessoal';
}

function renderTasks(userId) {
  const container = document.getElementById('task-list');
  const countEl = document.getElementById('task-count');
  const allTodos = getTodos().filter(t => t.userId === userId);

  // Active first, done at the end
  const active = allTodos.filter(t => !t.done);
  const done = allTodos.filter(t => t.done);
  const sorted = [...active, ...done];

  countEl.textContent = allTodos.length + (allTodos.length === 1 ? ' tarefa' : ' tarefas');

  if (sorted.length === 0) {
    container.innerHTML = `
      <div class="text-center py-10">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 mx-auto mb-3 text-slate-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
        <p class="text-slate-500 text-sm">Nenhuma tarefa cadastrada ainda.</p>
      </div>`;
    return;
  }

  container.innerHTML = sorted.map(task => {
    const badgeClass = getBadgeClass(task.type);
    const descHtml = task.description
      ? `<p class="text-slate-400 text-sm mt-1 leading-relaxed">${escapeHtml(task.description)}</p>`
      : '';

    const concludeLabel = task.done ? 'Reabrir' : 'Concluir';

    return `
      <div class="task-card ${task.done ? 'done' : ''}" id="task-${task.id}">
        <div class="flex items-start justify-between gap-3">
          <div class="flex-1 min-w-0">
            <div class="flex items-center gap-2 flex-wrap mb-1">
              <span class="task-title font-semibold text-white text-sm">${escapeHtml(task.title)}</span>
              <span class="text-xs px-2 py-0.5 rounded-full font-medium ${badgeClass}">${task.type}</span>
            </div>
            ${descHtml}
          </div>
          <div class="flex items-center gap-2 flex-shrink-0">
            <button onclick="handleToggleDone(${task.id})" class="btn-conclude">
              ${concludeLabel}
            </button>
            <button onclick="handleDeleteTask(${task.id})" class="btn-delete">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>`;
  }).join('');
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ──────────────────────────────────────────────
// INIT
// ──────────────────────────────────────────────

(function init() {
  const session = getSession();
  if (session) {
    loadDashboard(session);
  } else {
    showScreen('auth');
  }
})();
