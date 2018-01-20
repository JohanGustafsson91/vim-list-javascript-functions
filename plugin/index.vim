if !has('python3') && !has(python)
  echo "No python"
  finish
endif

function! FindFunctions()
  let g:currentFileFindFunctions = shellescape(expand('%'))
  execute (has('python3') ? 'py3file ' : 'pyfile ') './plugin/index.py'
endfunc

nmap <silent> <C-a>f :call FindFunctions()<CR>
