module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
    // {
    //   polyfills: [
    //     'es6.promise',
    //     'es6.symbol'
    //   ]
    // }
  ],
  plugins: [
    [
      'component',
      {
        libraryName: 'element-ui',
        styleLibraryName: 'theme-chalk'
      }
    ]
  ]
}
