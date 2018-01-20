# vim-list-javascript-functions
List all javascript functions in current file

![Gif showing plugin](https://thumbs.gfycat.com/OfficialEnviousIlsamochadegu-size_restricted.gif)

## Installation

Use your plugin manager of choice.

- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'JohanGustafsson91/vim-list-javascript-functions'`
  - Run `:BundleInstall`

## Basic usage
1. Press `<CTRL+a>f` in file
2. Watch output of found functions
3. Go to line (optional)

## Basic options

#### Set file path to python script
Default is `~/.vim/bundle/vim-list-javascript-functions/plugin/`

```
let g:vim_list_javascript_functions_filepath = 'new/file/path/'
```

#### TODOs
- [ ] Add support for filename extensions
- [ ] Add support for user defined shortcut command

