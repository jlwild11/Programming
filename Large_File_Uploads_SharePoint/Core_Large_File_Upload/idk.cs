public void UploadDocumentContent(ClientContext ctx, string libraryName, string filePath)
{
  Web web = ctx.Web;

  // Ensure that target library exists. Create if it is missing.
  if (!LibraryExists(ctx, web, libraryName))
  {
    CreateLibrary(ctx, web, libraryName);
  }

  FileCreationInformation newFile = new FileCreationInformation();

  // The next line of code causes an exception to be thrown for files larger than 2 MB.
  newFile.Content = System.IO.File.ReadAllBytes(filePath);
  newFile.Url = System.IO.Path.GetFileName(filePath);

  // Get instances to the given library.
  List docs = web.Lists.GetByTitle(libraryName);

  // Add file to the library.
  Microsoft.SharePoint.Client.File uploadFile = docs.RootFolder.Files.Add(newFile);
  ctx.Load(uploadFile);
  ctx.ExecuteQuery();
}